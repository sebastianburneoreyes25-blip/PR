<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/Ejercicio16MVC/app/vistas/style.css">
</head>

<body>
    <?php if (!empty($error)): ?>
        <div class="error">
            <p><?php echo htmlspecialchars($error) ?></p>
        </div>
    <?php endif ?>
    <?php if (!empty($alumno)): ?>
        <div class="contenedor">
            <table>
                <thead>
                    <tr>
                        <td>Nombre</td>
                        <td>Email</td>
                        <td>Edad</td>
                        <td>Acciones</td>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <form action="/Ejercicio16MVC/public/index.php?accion=enviar" method="POST">
                            <input 
                            type="hidden" value="<?php echo htmlspecialchars($alumno->id)?>" 
                            name="id" >
                            <td><input type="text" value="<?php echo htmlspecialchars($alumno->nombre) ?>" name='nombre'></td>
                            <td><input type="text" value="<?php echo htmlspecialchars($alumno->email) ?>" name='email'></td>
                            <td><input type="text" value="<?php echo htmlspecialchars($alumno->edad) ?>" name='edad'></td>
                            <input type="hidden" value="<?php echo htmlspecialchars($alumno->fecha_creacion)?>" 
                            name="fecha_creacion">
                            <td><input type="submit" value="Enviar"></td>
                        </form>
                    </tr>
                </tbody>
        </div>
    <?php endif ?>
</body>

</html>