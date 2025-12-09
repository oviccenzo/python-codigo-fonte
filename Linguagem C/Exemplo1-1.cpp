//
// Created by Robert L Resende on 24/09/25.
//
#include "raylib.h"

int main(void)
{
    // Inicializa a janela e o contexto OpenGL
    const int screenWidth = 800;
    const int screenHeight = 450;

    InitWindow(screenWidth, screenHeight, "Gerar Imagem com CLion");

    // Cria uma imagem em memória
    Image image = GenImageColor(screenWidth, screenHeight, RED);
    ExportImage(image, "minha_imagem.png"); // Salva a imagem num ficheiro

    UnloadImage(image); // Liberta a memória da imagem

    CloseWindow(); // Fecha a janela

    return 0;
}