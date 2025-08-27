
class AlumnoValidator:

    @staticmethod
    def validate_alumno(data):
        errors = []
        if not data.get('nombre'):
            errors.append('El nombre es obligatorio.')
        if not data.get('dni'):
            errors.append('El DNI es obligatorio.')
        
        return errors
