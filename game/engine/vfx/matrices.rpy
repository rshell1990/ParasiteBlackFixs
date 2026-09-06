init -2 python:
    class MxDayNight(ColorMatrix):
        def get(self, value):
            InvertedValue = 1.0 - value
            return Matrix([ 0.45 + 0.55 * value, 0.0, 0.0, -0.03 * InvertedValue,
                            0.0, 0.45 + 0.55 * value, 0.0, -0.03 * InvertedValue,
                            0.0, 0.0, 0.75 + 0.25 * value, -0.03 * InvertedValue,
                            0.0, 0.0, 0.0, 1.0])

    class MxDayNight_Desert(ColorMatrix):
        def get(self, value):
            InvertedValue = 1.0 - value
            return Matrix([ 0.45 + 0.55 * value, 0.0,  0.0,  -0.2 * InvertedValue,
                            0.0,  0.45 + 0.55 * value, 0.0,  -0.1 * InvertedValue,
                            0.05 * InvertedValue, 0.05 * InvertedValue, 0.75 + 0.25 * value, -0.025 * InvertedValue,
                            0.0,  0.0, 0.0,   1.0])

    class MxWarm(ColorMatrix):
        def get(self, value):
            return Matrix([ 1.0, 0.0, 0.0, 0,
                            0.0, 0.8, 0.0, 0,
                            0.0, 0.0, 0.6, 0,
                            0.0, 0.0, 0.0, 1.0])

    class MxMapHover(ColorMatrix):
        def get(self, value):
            return Matrix([ 1.1, 0.0, 0.0, 0.2,
                            0.0, 1.1, 0.0, 0.2,
                            0.0, 0.0, 1.1, 0.2,
                            0.0, 0.0, 0.0, 1.0])

    class MxNight(ColorMatrix):
        def get(self, value):
            return Matrix([ 0.45, 0.0, 0.0, -0.03,
                            0.0, 0.45, 0.0, -0.03,
                            0.0, 0.0, 0.75, -0.03,
                            0.0, 0.0, 0.0, 1.0, ])