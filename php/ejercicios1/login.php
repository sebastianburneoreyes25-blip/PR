    <?php
    $user=["admin"=>"123456", "Pablo"=>"Motos", "Carol"=>"holaPitufo"];//Aqui tenemos las listas con los usuarios  contraseñas
    $usuario=$_POST['usuario'];
    $pass=$_POST['clave'];
    $flag=false;//la 
    foreach ($user as $u=>$pss){//recorremos la lista de usuarios para comprobar si la clave y el valor coinciden
        if($u==$usuario and $flag==false){
            if ($pss==$pass and $flag==false){
                echo"<h3> Bienvenido</h3>";
                $flag=true;
            }
        }
    }
    if ($flag==false){//Si no coincide usuario o contraseña saldra este mensaje 
        echo"<h3> Usuario o contraseña erroneo</h3>";
    }
    ?>