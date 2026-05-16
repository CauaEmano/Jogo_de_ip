#ifndef TIRO_H
#define TIRO_H

#include "Projetil.hpp"

class Tiro : public Projetil{
    public:
        Tiro(float pos_x, float pos_y, int direcao);
        ~Tiro();

        void update() override;
        void ricochetear(); // verificar se o tiro bateu na parede e ricochetear
};

#endif