#include <stdio.h>
#include <string.h>

// Estrutura para armazenar as informações do cliente
struct Cliente {
    char nome[50];
    char telefone[15];
    char nomedaEmpresa[50];
    char email[50];
    char aniversario[6]; // Considerando dia/mês, como 01/12
    // Outras informações podem ser adicionadas aqui
};

// Variável para armazenar os clientes
struct Cliente clientes[100];
int numClientes = 0;

// Função para inserir um novo cliente
void inserirCliente() {
    struct Cliente novoCliente;
    printf("Nome: ");
    scanf("%s", novoCliente.nome);
    printf("Telefone: ");
    scanf("%s", novoCliente.telefone);
    printf("Nome da Empresa: ");
    scanf("%s", novoCliente.nomedaEmpresa);
    printf("E-mail: ");
    scanf("%s", novoCliente.email);
    printf("Data de Aniversário (dia/mês, ex: 01/12): ");
    scanf("%s", novoCliente.aniversario);

    clientes[numClientes] = novoCliente;
    numClientes++;
    printf("Cliente adicionado com sucesso!\n");
}

// Função para listar todos os clientes em ordem alfabética por nome
void listarClientes() {
    // Ordenar os clientes por nome em ordem alfabética
    for (int i = 0; i < numClientes - 1; i++) {
        for (int j = 0; j < numClientes - i - 1; j++) {
            if (strcmp(clientes[j].nome, clientes[j + 1].nome) > 0) {
                struct Cliente temp = clientes[j];
                clientes[j] = clientes[j + 1];
                clientes[j + 1] = temp;
            }
        }
    }

    // Exibir os clientes ordenados
    printf("Listagem de clientes por nome:\n");
    for (int i = 0; i < numClientes; i++) {
        printf("Nome: %s, Telefone: %s, Empresa: %s, E-mail: %s, Aniversario: %s\n",
               clientes[i].nome, clientes[i].telefone, clientes[i].nomedaEmpresa,
               clientes[i].email, clientes[i].aniversario);
    }
}

// Função para salvar os clientes em um arquivo
void salvarClientes() {
    FILE *trabalhotxt;
    FILE *arquivo = fopen("clientes.txt", "w");
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return;
    }

    for (int i = 0; i < numClientes; i++) {
        fprintf(arquivo, "%s %s %s %s %s\n", clientes[i].nome, clientes[i].telefone,
                clientes[i].nomedaEmpresa, clientes[i].email, clientes[i].aniversario);
    }

    fclose(arquivo);
}

// Função para carregar os clientes de um arquivo
void carregarClientes() {
    FILE *arquivo;
    arquivo = fopen("clientes.txt", "r");
    if (arquivo == NULL) {
        printf("Arquivo de cliente não encontrado ou vazio.\n");
        return;
    }

    while (fscanf(arquivo, "%s %s %s %s %s", clientes[numClientes].nome, clientes[numClientes].telefone,
                  clientes[numClientes].nomedaEmpresa, clientes[numClientes].email, clientes[numClientes].aniversario) != EOF) {
        numClientes++;
    }

    fclose(arquivo);
}

// Função principal (menu)
int main() {
    carregarClientes(); // Carregar os clientes do arquivo, se existirem

    int opcao;
    do {
        printf("\nSelecione uma opção:\n");
        printf("1 - Inserir novos clientes\n");
        printf("2 - Alterar dados de um cliente\n");
        printf("3 - Excluir um cliente\n");
        printf("4 - Listagem de todos os clientes em tela por nome (ordem alfabética)\n");
        printf("5 - Pesquisa de clientes pelo nome da empresa\n");
        printf("6 - Pesquisar cliente\n");
        printf("7 - Salvar dados dos clientes no arquivo\n");
        printf("0 - Sair\n");
        scanf("%d", &opcao);

        switch(opcao) {
            case 1:
                inserirCliente();
                break;
            case 4:
                listarClientes();
                break;
            case 7:
                salvarClientes();
                printf("Dados dos clientes salvos com sucesso!\n");
                break;
            // Implementar outras funcionalidades aqui
            // ...
            case 0:
                printf("Encerrando o programa.\n");
                break;
            default:
                printf("Opção inválida.\n");
        }
    } while (opcao != 0);

    return 0;
}




