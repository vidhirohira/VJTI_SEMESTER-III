#include <iostream>
#include <iomanip> 
using namespace std;

void spi_calc() {
    cout << "Enter number of subjects:" << endl;
    int n;
    cin >> n;

    int* credit = new int[n+1];
    int* grade = new int[n+1];

    for (int i = 1; i <= n; i++) {
        cout << "Enter credit and grade for subject " << i << endl;
        cin >> credit[i] >> grade[i];
        if (grade[i] < 0) {
            cout << "ERROR! Grade cannot be negative." << endl;
            delete[] credit; 
            delete[] grade;  
            return;
        }
    }

    // Calc
    int tot_scr = 0;
    int tot_cred = 0;
    for (int i = 1; i <= n; i++) {
        tot_scr += grade[i] * credit[i];
        tot_cred += credit[i];
    }

    // Result
    float SPI = 1.0 * tot_scr / tot_cred;
    cout << fixed << setprecision(2) << "Your SPI is: " << SPI << endl;

    delete[] credit;
    delete[] grade;
}

void cpi_calc() {
    cout << "Enter number of semesters:" << endl;
    int n;
    cin >> n;

    float* spi_values = new float[n+1];

    for (int i = 1; i <= n; i++) {
        cout << "Enter SPI for semester " << i << endl;
        cin >> spi_values[i];
        if (spi_values[i] < 0) {
            cout << "ERROR! SPI cannot be negative." << endl;
            delete[] spi_values;    
            return; 
        }
    }

    // Calc
    float total_spi = 0;
    for (int i = 1; i <= n; i++) {
        total_spi += spi_values[i];
    }

    // Result cppi
    float CPI = total_spi / n;
    cout << fixed << setprecision(2) << "Your CPI is: " << CPI << endl;

    delete[] spi_values;
}

int main() {
    spi_calc();
    cpi_calc();
    return 0;
}