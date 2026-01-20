<?php



class Carrito{

    public $productos = [];



    public function agregarProcuto($nombre, $precioUnitario, $cantidad){

        $producto = [$nombre, $precioUnitario, $cantidad];
        array_push($this->productos, $producto);
    }
    public function quitarProducto($nombre){
        foreach ($this->productos as [$nombreProducto, $precio, $cantidad]) {
            $n = 0;
            if ($nombre == $nombreProducto) {
                unset($this->productos[$n]);
            }
            $n++;
        }
    }
    public function mostrarDetalle(){
        foreach ($this->productos as [$nombreProducto, $precio, $cantidad]) {
            echo $nombreProducto . "\n";
            echo $precio . "€ \n";
            echo $cantidad . "\n";
        }
    }
    public function calcularTotal(){
        foreach ($this->productos as [$nombreProducto, $precio, $cantidad]) {
            $total = $precio * $cantidad;
        }
        return $total;
    }
}
