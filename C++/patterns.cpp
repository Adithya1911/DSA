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
int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    // printRectangularStarPattern(n);
    // printTriangularStarPattern(n);
    // printTriangularNumberPattern(n);
    // printTriangularNumberPattern2(n);
    printInverseTriangularStar(n);
    return 0;
}
