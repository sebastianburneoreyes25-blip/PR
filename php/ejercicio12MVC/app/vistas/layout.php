<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    
<div>
        <header>
            <h1>Menú</h1>
        </header>
        <nav>
            <ul>
                <li><a href="/ejercicio12MVC/public/index.php?accion=listar">Listar </a></li>
                <li><a href="/ejercicio12MVC/public/index.php?accion=crear">Crear </a></li>
            </ul>
        </nav>
    </div>
    <?php
    
    if(!empty($contenidoVista)){
    require $contenidoVista;
    }
    ?>
</body>
</html>