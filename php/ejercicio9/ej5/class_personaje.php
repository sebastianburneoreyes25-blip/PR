<?php

class Personaje
{ //definimos atributos y metodos de la classe

    public $nombre;
    public $nivel;
    public $puntosVida;
    public $puntosAtaque;

    public function ataque($objetivo)
    {

        if ($objetivo->puntosVida > 0) {
            $objetivo->puntosVida -= $this->puntosAtaque;
            echo $this->nombre . " ha quitado a " . $objetivo->nombre . " " . $this->puntosAtaque . " puntos de vida.\n\n";
            if ($objetivo->puntosVida <= 0) { //si muere o esta ya muerto anteriormente el personaje objetivo, lanzará el mensaje siguiente:
                echo $objetivo->puntosVida . " ha muerto o quedado inconsciente.\n\n";
            }
        } else {
            echo $objetivo->puntosVida . " está muerto o inconsciente.";
        }
    }
    public function curarse()
    {
        $cura = $this->nivel * rand(1, 10);
        $this->puntosVida += $cura;
        echo $this->nombre . " se hacurado $cura puntos de vida.\n\n";
    }
    public function subir_nivel()
    {
        $this->nivel++;
        $this->puntosVida += rand(1, 10);
        $this->puntosAtaque += rand(3, 5);
        echo $this->nombre . " ha subido de nivel\n\n";
    }
}
