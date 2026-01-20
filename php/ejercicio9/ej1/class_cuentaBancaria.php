<?php

class CuentaBancaria{
    public  $titular;
    public $saldo;
    public $tipoDeCuenta;

    public function depositar($cantidad){
        $this->saldo+=$cantidad;
        echo"Se ha depositado $cantidad €";
    }
    public function retirar($cantidad){
        $this->saldo-=$cantidad;
        echo"Se ha retirado $cantidad";
    }
    public function consultarDatos(){
        echo"Titular:".$this->titular. PHP_EOL;
        echo"Tipo de cuenta:".$this->tipoDeCuenta. PHP_EOL;
        echo"Saldo actual:". $this->saldo."€". PHP_EOL;
    }
}

?>