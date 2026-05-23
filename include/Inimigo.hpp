#ifndef INIMIGO_H
#define INIMIGO_H

#include <string>

class Inimigo {
    private:
        std::string nome;
        double vida;
        double dano; 
        double posicao_x; //posições para inimigos no mapa
        double posicao_y;
        

    public:
        Inimigo(std::string n, double v, double d, double x, double y) : nome(n), vida(v), dano(d), posicao_x(x), posicao_y(y){}
        virtual ~Inimigo() {}

        //ações
        virtual void atacar() =0; //método virtual puro, permite às classes filhas terem diferentes maneiras de atacar
        void receberDano(int qtd); 
        void mostrarStatus() const;

        std::string getNome()const {return nome;};
        double getVida() const {return vida;};
        double getDano() const {return dano;};
        double getPosicaoX() const {return posicao_x;};
        double getPosicaoY() const {return posicao_y;};

};


#endif