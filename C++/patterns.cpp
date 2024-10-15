// Pattern-1: Rectangular Star Pattern
// In this problem you need to print the pattern of stars in the square of size nxn matrix

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

void printRectangularStarPattern(int n) {
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

void printTriangularStarPattern(int n) {
    for (int i=0; i<n; i++) {
        for (int j=0; j<=i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

void printTriangularNumberPattern(int n) {
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=i; j++) {
            cout << i << " ";
        }
        cout << endl;
    }
}

void printTriangularNumberPattern2(int n) {
    for (int i=1; i<=n; i++) {
        for (int j=1; j<=i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
}

void printTriangularInverse(int n){
    for (int i=n; i>=1; i--) {
        for (int j=1; j<=i; j++) {
            cout << j << " ";
        }
        cout << endl;
    }
}

void printInverseTriangularStar(int n){
    for (int i=n;i>=1;i--){
        for (int j=1;j<=i;j++){
            cout <<"* ";
        }
        cout << endl;
    }
}

void printInverseTriangularNumber(int x){
    for (int i=x;i>=1;i--){
        for (int j=1;j<=i;j++){
            cout << j << " ";
        }
        cout << endl;
    }
}

void printTriangularPiramid(int x){
    for(int i=x;i>=1;i--){
        for(int j=1;j<i;j++){
            cout << " ";
        }
        for(int j=2*(x-i)+1;j>0;j--){
            cout << "*";
        }
        cout << endl;
    }
}

void printInvertedTriangularPiramid(int x){
    for(int i=1;i<=x;i++){
        for(int j=1;j<i;j++){
            cout << " ";
        }
        for(int j=2*(x-i)+1;j>0;j--){
            cout << "*";
        }
        cout << endl;
    }
}

void printNStarPattern(int x){
    for(int i=x;i>=1;i--){
        for(int j=1;j<i;j++){
            cout << " ";
        }
        for(int j=2*(x-i)+1;j>0;j--){
            cout << "*";
        }
        cout << endl;
    }
    for(int i=1;i<=x;i++){
        for(int j=1;j<i;j++){
            cout << " ";
        }
        for(int j=2*(x-i)+1;j>0;j--){
            cout << "*";
        }
        cout << endl;
    }
}
int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    // printRectangularStarPattern(n);
    // printTriangularStarPattern(n);
    // printTriangularNumberPattern(n);
    // printTriangularNumberPattern2(n);
    // printInverseTriangularStar(n);
    // printInverseTriangularNumber(n);
    // printTriangularPiramid(n);
    // printInvertedTriangularPiramid(n);
    printNStarPattern(n);
    return 0;
}
