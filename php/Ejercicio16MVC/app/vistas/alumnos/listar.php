<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="/Ejercicio16MVC/app/vistas/style.css">
</head>
<body>
    <?php if(!empty($error)):?>
        <div class="error">
            <p><?php echo htmlspecialchars($error)?></p>
        </div>
    <?php endif?>
    <?php if(!empty($alumnos)):?>
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
                    <?php foreach($alumnos as $a):?>
                        <tr>
                            <td><?php echo htmlspecialchars($a->nombre)?></td>
                            <td><?php echo htmlspecialchars($a->email)?></td>
                            <td><?php echo htmlspecialchars($a->edad)?></td>
                            <td><button><a href="/Ejercicio16MVC/public/index.php?accion=editar&id=<?php echo htmlspecialchars($a->id)?>">Editar</a></button></td>

                        </tr>
                    <?php endforeach?>
                </tbody>
            </table>
        </div>
        <?php endif?>
</body>
</html>