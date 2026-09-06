init -1 python:
    # If an expression is false, throw exception string. Is pmuch a shorthand
    def Assert(Expression, ExceptionString = "ERROR"):
        if config.developer:
            if Expression is not True:
                raise Exception(ExceptionString)
        return