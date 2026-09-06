# THIS PLUGIN IMPROVES THE EFFECT OF REN'PY'S STANDARD BLUR
# i didnt add this and i dont know where or how we're even using this -tmm

default preferences.graphics_blur = 2  # 0-2

init python hide:

    ############################################################################
    # Disable Ren'Py blur

    renpy.register_shader("renpy.blur", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_renpy_blur_log2;

    """, vertex_200="""
        v_tex_coord = a_tex_coord;

    """, fragment_200="""
        gl_FragColor = texture2D(tex0, v_tex_coord.xy);
    """)


    #############################################################################
    # Default Ren'Py blur

    renpy.register_shader("_renpy.blur", variables="""
        uniform sampler2D tex0;
        uniform vec2 res0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_renpy_blur_log2;

    """, vertex_200="""
        v_tex_coord = a_tex_coord;

    """, fragment_200="""
        gl_FragColor = vec4(0.0);
        float renpy_blur_norm = 0.0;

        for (float i = -5.0; i < 1.0; i += 1.0) {
            float renpy_blur_weight = exp(-0.5 * pow(u_renpy_blur_log2 - i, 2.0));
            renpy_blur_norm += renpy_blur_weight;
        }

        gl_FragColor += renpy_blur_norm * texture2D(tex0, v_tex_coord.xy, 0.0);

        for (float i = 1.0; i < 14.0; i += 1.0) {

            if (i >= u_renpy_blur_log2 + 5.0) {
                break;
            }

            float renpy_blur_weight = exp(-0.5 * pow(u_renpy_blur_log2 - i, 2.0));
            gl_FragColor += renpy_blur_weight * texture2D(tex0, v_tex_coord.xy, i);
            renpy_blur_norm += renpy_blur_weight;

        }

        if (renpy_blur_norm > 0.0) {
            gl_FragColor /= renpy_blur_norm;
        } else {
            gl_FragColor = texture2D(tex0, v_tex_coord.xy, 0.0);
        }
    """)


    ############################################################################
    # Noisy Blur

    renpy.register_shader(
        "renpy.noisy_blur",

    variables="""
        uniform float u_blur;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform float u_time;
        uniform sampler2D tex0;
        uniform vec2 res0;
    """,

    vertex_200="""
        v_tex_coord = a_tex_coord;
    """,

    fragment_functions="""
        float rand(vec2 uv)
        {
            return fract(cos(dot(uv, vec2(12.9898, 78.233))) * 43578.5453) * 2.0 - 1.0;
        }
    """,

    fragment_200="""
        gl_FragColor = vec4(0.0);
        const int loops = 8; // more loops => more GPU load

        const float PI = 3.1415926535897932384626433832795;
        float step = (2.0 * PI) / float(loops);
        vec2 texel = res0 / (u_blur * .5);

        if (u_blur > 0.0) {

            for(int i = 1; i <= loops; i++){
                float rx = clamp(rand(u_time * v_tex_coord * float(i)), -texel.x, texel.x);
                float ry = clamp(rand(u_time * v_tex_coord * float(i + loops)), -texel.y, texel.y);

                rx += sin(step * float(i));
                ry += cos(step * float(i));

                gl_FragColor += texture2D(tex0, v_tex_coord + vec2(rx , ry) / texel, 0.0);
            }

            gl_FragColor /= float(loops);

        } else {
            gl_FragColor = texture2D(tex0, v_tex_coord);
        }

    """)


    ############################################################################
    # Gaussian blur

    renpy.register_shader("shader.gaussian", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_blur;
        uniform vec2 u_direction;

    """, vertex_200="""
        v_tex_coord = a_tex_coord;

    """, fragment_200="""
        gl_FragColor = vec4(0.0);
        const float PI = 3.1415926535897932384626433832795;
        float pow_sigma = pow(u_blur * .5, 2.0);
        float weigth = 1.0 / sqrt(2.0 * PI * pow_sigma);

        if (u_blur > 0.0) {
            float renpy_blur_norm = 0.0;

            for (float offset = -u_blur; offset <= u_blur; offset++) {
                float renpy_blur_weight = weigth * exp(-(offset * offset) / (2.0 * pow_sigma));
                gl_FragColor += renpy_blur_weight * texture2D(tex0, v_tex_coord + vec2(offset * clamp(u_blur - 0.5, 0.0, 1.0)) * u_direction / res0.xy, 0.0);
                renpy_blur_norm += renpy_blur_weight;
            }

            gl_FragColor /= renpy_blur_norm;

        } else {
            gl_FragColor = texture2D(tex0, v_tex_coord, 0.0);
        }
    """)


    ############################################################################

    from renpy.display.accelerator import RenderTransform

    def render(self, width, height, st, at):

        # Just a copy of the `renpy.display.Transform.render` function:
        if st + self.st_offset <= self.st:
            self.st_offset = self.st - st
        if at + self.at_offset <= self.at:
            self.at_offset = self.at - at

        self.st = st = st + self.st_offset
        self.at = at = at + self.at_offset

        self.update_state()

        rv = RenderTransform(self).render(width, height, st, at)
        # Copy end.

        ########################################################################
        # Gaussian

        def gaussian_blur(rv, blur):

            def apply(rv, shader, blur, direction):
                cr = rv

                rv = renpy.Render(*cr.get_size())
                rv.mesh = True
                rv.blit(cr, (0, 0))
                rv.add_shader("-renpy.texture")

                rv.add_shader(shader)
                rv.add_uniform("u_blur", blur)
                rv.add_uniform("u_direction", direction)
                return rv

            rv = apply(rv, "shader.gaussian", blur, direction=(1.0, 0.0))
            rv = apply(rv, "shader.gaussian", blur, direction=(0.0, 1.0))

            return rv

        ########################################################################
        # Noisy

        def noisy_blur(rv, blur):
            cr = rv

            rv = renpy.Render(*cr.get_size())
            rv.mesh = True
            rv.blit(cr, (0, 0))
            rv.add_shader("-renpy.texture")

            rv.add_shader("renpy.noisy_blur")
            rv.add_uniform("u_blur", blur)
            return rv

        ########################################################################
        # Default

        def renpy_blur(rv, blur):
            cr = rv

            rv = renpy.Render(*cr.get_size())
            rv.mesh = True
            rv.blit(cr, (0, 0))
            rv.add_shader("-renpy.texture")

            rv.add_shader("_renpy.blur")
            rv.add_uniform("u_renpy_blur_log2", math.log(blur * 1.25, 2))
            return rv

        ########################################################################
        # Apply Blur

        blur = (self.state.blur or None)
        graphics_blur = preferences.graphics_blur

        if blur is not None:

            if graphics_blur == 2:
                rv = gaussian_blur(rv, blur)    # 17.0%         36.0%  <-- High GPU load

            elif graphics_blur == 1:
                rv = noisy_blur(rv, blur)       # 13.0%         17.0%

            elif graphics_blur == 0:
                rv = renpy_blur(rv, blur)       # 9.0%          9.0%

        return rv

    renpy.display.transform.Transform.render = render