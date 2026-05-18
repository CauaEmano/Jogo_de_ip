#ifndef JOGADOR_H
#define JOGADOR_H

#include <iostream>
#include <map>
#include <string>
#include <vector>

class Projetil;

class Jogador{
    private:
        int vida; 
        int max_vida;

        float pos_x, pos_y; 
        float vel_x, vel_y;  
        int direcao; 

        int invencib_timer;
        int tiro_cooldown; 
        bool no_ar; 
        bool pulo_duplo; 

        std::map<std::string, int> inventario; 

    public:
        Jogador(int max_vida, float pos_x, float pos_y, float vel_x, float vel_y); 
        void mover(int direcao);
        void pular();

        void receberDano(int quantidade);
        void atirar(std::vector<Projetil*>& balas);
        bool isVivo() const;
        void adicionarItem(std::string item, int quantidade);
        int getItem(std::string item) const;
        void update();

        int getDirecao() const;
        float getPosX() const;
        float getPosY() const;

        friend std::ostream& operator<<(std::ostream& os, const Jogador& j);
};

#endif