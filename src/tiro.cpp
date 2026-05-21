#include "Tiro.hpp"


Tiro::Tiro(float pos_x, float pos_y, int direcao) : Projetil(pos_x, pos_y, 10.0f * direcao, 0.0f, 5) {
}

Tiro::~Tiro() {
}

void Tiro::ricochetear(float parede_esquerda, float parede_direita) {

    if (this->pos_x >= parede_direita) {
        this->pos_x = parede_direita; 
        this->vel_x = -this->vel_x;
    }

    else if (this->pos_x <= parede_esquerda) {
        this->pos_x = parede_esquerda;
        this->vel_x = -this->vel_x;    
    }
}

void Tiro::update() {
    this->vel_y -= 0.2f; // obs: ajustar gravidade depois.
    
    this->pos_x += this->vel_x; 
    this->pos_y += this->vel_y; 

    ricochetear(0.0, 0.0); // ajustar limites na main

    if (this->pos_y <= 0.0f) {
        this->pos_y = 0.0f; 
        desativar();
    }
}

void Tiro::desativar() {
    Projetil::desativar();
    // lógica para virar coletável será implementada posteriormente.
}