#ifndef PROJETIL_H
#define PROJETIL_H

class Projetil{
    protected:
        float pos_x, pos_y;
        float vel_x, vel_y;
        int dano;
        bool ativo; // se o projétil já colidiu com algo ou ainda está ativo.
    public:
        Projetil(float pos_x, float pos_y, float vel_x, float vel_y, int dano);
        virtual ~Projetil();

        virtual void update() = 0;
        int getDano() const;
        float getPosX() const;
        float getPosY() const;

        bool isAtivo() const;
        void desativar();
};

#endif