package com.pao.laboratory00;
import java.util.Scanner;
/**
 * Exercitiul 2
 *
 * Cititi de la tastatura o matrice de n ori n elemente REALE.
 *
 * 1. Afisati matricea in consola.
 * 2. Afisati suma elementelor de pe diagonala principala
 *    si produsul elementelor de pe diagonala secundara.
 *
 */

public class DiagonaleleMatricei {
    public static void main(String[] args) {
        int n;
        double s=0,p=1;
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        double[][] mat = new double[n][n];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                mat[i][j] = scanner.nextInt();
            }
        }
        for(int i=0;i<n;i++)
        {
            s+=mat[i][i];
            p*=mat[i][n-1-i];
            for(int j=0;j<n;j++)
            {
                System.out.println(mat[i][j]);
            }
        }
        System.out.println(s);
        System.out.println(p);
    }
}
