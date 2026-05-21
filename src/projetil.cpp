#include "Projetil.hpp"

Projetil::Projetil(float pos_x, float pos_y, float vel_x, float vel_y, int dano){
    this->pos_x = pos_x;
    this->pos_y = pos_y;
    this->vel_x = vel_x;
    this->vel_y = vel_y;
    this->dano = dano;
    this->ativo = true;
}

Projetil::~Projetil(){
}

int Projetil::getDano() const{
    return(dano);
}

float Projetil::getPosX() const{
    return(pos_x);
}

float Projetil::getPosY() const{
    return(pos_y);
}

bool Projetil::isAtivo() const{
    return(ativo);
}

void Projetil::desativar(){
    this->ativo = false;
}