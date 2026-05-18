#include "Jogador.hpp"
#include "Pedra.hpp"
#include "Tiro.hpp"

Jogador::Jogador(int max_vida, float pos_x, float pos_y, float vel_x, float vel_y){
    this->max_vida = max_vida;
    this->vida = max_vida;
    this->pos_x = pos_x;
    this->pos_y = pos_y;
    this->vel_x = vel_x;
    this->vel_y = vel_y;
    this->direcao = 1;
    invencib_timer = 0;
    tiro_cooldown = 0;
    no_ar = false;
    pulo_duplo = true;
    inventario.insert({"Pedra", 8});
}

void Jogador::mover(int direcao){
    this->direcao = direcao;
    this->pos_x += (vel_x*direcao);
}

void Jogador::pular(){
    if(no_ar == true){
        if(pulo_duplo == true){
            pos_y += vel_y;
            pulo_duplo = false;
        }
    }
    else{
        no_ar = true;
        pulo_duplo = true;
        pos_y += vel_y;
    }
}

void Jogador::receberDano(int quantidade){
    if(invencib_timer == 0){
        this-> vida -= quantidade;
        invencib_timer = 2;
    }
}

void Jogador::atirar(std::vector<Projetil*>& balas){
    if(tiro_cooldown > 0 || inventario["Pedra"] == 0){
        return;
    }
    else{
        inventario["Pedra"] -= 1;
        tiro_cooldown = 2;
        Tiro* pedra = new Tiro(this->pos_x, this->pos_y, direcao);
        balas.push_back(pedra);
    }
}

bool Jogador::isVivo() const{
    if(vida > 0){
        return true;
    }
    else{
        return false;
    }
}

void Jogador::adicionarItem(std::string item, int quantidade){
    inventario[item] += quantidade;
}

int Jogador::getItem(std::string item) const{
    return(inventario.at(item));
}

int Jogador::getDirecao() const{
    return(this->direcao);
}

float Jogador::getPosX() const{
    return(this->pos_x);
}

float Jogador::getPosY() const{
    return(this->pos_y);
}

// FALTA IMPLEMENTAR O update() e o <<. Farei depois.
