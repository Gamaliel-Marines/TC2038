#include <iostream>
#include <string>




void createLaberinth(int n, int m){
    int laberinth[n][m];
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            int temp;
            std::cout <<"Ingrese el valor de la posicion ["<<i<<"]["<<j<<"]: ";
            std::cin >>temp;
            if(temp != 0 && temp != 1)
            {
                std::cout <<"Ingrese un valor valido (0 o 1)"<<std::endl;
                j--;

            }
            else
            laberinth[i][j] = temp;
        }
    }
    /**
     * @brief print matrix
     * @param n number of rows
     * @param m number of columns
     * @param laberinth matrix
     * @return void
     */
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            std::cout << laberinth[i][j] << " ";
            
        }
        std::cout <<std::endl;
    }

    
    
}

void findPath()
{

}

int main()
{
    int n, m;
    std::cout <<"Ingrese el numero de filas: ";
    std::cin >>n;
    std::cout <<"Ingrese el numero de columnas: ";
    std::cin >>m;
    createLaberinth(n, m);
    return 0;
}
