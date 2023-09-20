from generator.utils import snake_case, pascal_case, camel_case, is_builtin


class ExtendedString(str):
    @property
    def camel_case(self):
        return camel_case(self)

    @property
    def pascal_case(self):
        return pascal_case(self)

    @property
    def snake_case(self):
        return snake_case(self)

    @property
    def snake_case_non_colliding(self):
        name = self.snake_case
        if is_builtin(name):
            name += '_'
        return name
