<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
        <link rel="stylesheet" href="style.css">

</head>

<body>
    </table>
    <?php
   require_once __DIR__."/../../modelos/repositorioTarea.php";
    $tabla = "<table border='2'><tr><td>ID</td><td>Tarea</td><td>Estado</td><td>Fecha de creación</td></tr>";
    $tareas = new RepositorioTarea;
    $arrayTareas = $tareas->obtenerTareas();
    if (empty($arrayTareas)) {
        echo "<h2>No hay tareas para listar</h2>";
    } else {
     
        foreach ($arrayTareas as $tareaObjeto) {
            $id=$tareaObjeto->getId();
            $titulo= $tareaObjeto->getTitulo() ;
            $estado=$tareaObjeto->getEstado() ;
            $fecha=$tareaObjeto->getFecha() ;
            $tabla .= "<tr><td>$id</td><td>$titulo</td><td>$estado</td><td>$fecha</td></tr>";
        }
        $tabla .= "</table>";
        echo $tabla;
    }


    ?>
</body>

</html>