package com.pao.laboratory00;

import java.util.Scanner;
/**
 * Exercitiul 1
 *
 * Cititi de la tastatura un sir cu n elemente intregi.
 *
 * 1. Afisati elementele sirului in doua modalitati.
 * 2. Afisati media aritmetica a elementelor sirului.
 *
 */

public class MediaAritmetica {
    public static void main(String[] args) {
        int[] array;
        int n,s=0;
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        array = new int[n];
        for(int i=0;i<n;i++)
        {
            array[i] = scanner.nextInt();
        }
        for(int i=0;i<n;i++)
        {
            System.out.println(array[i]);
        }
        for(int x:array)
        {
            System.out.println(x);
            s+=x;
        }
        System.out.println((double)s/n);
    }
}
