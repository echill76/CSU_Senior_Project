#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <iomanip> // for std::fixed and std::setprecision

using namespace std;

struct Career {
    string name;
    double income;
    double taxes;
    double loan;
    double tithing;
};

/*Displays a running counter of the player's budget
* each time a change in the budget happens.
*/
void displayBudget(double budget);

// Handles the Random Events
double flipCoinEvent(string heads, double headsAmount, string tails, double tailsAmount, double &budget);

int main() {
    srand(time(0));

    Career careers[] = {
        {"No College", 2000, 200, 0, 180},
        {"Certificate", 3500, 350, 160, 315},
        {"Undergraduate", 5200, 520, 310, 468},
        {"Graduate", 7000, 700, 440, 630},
        {"Doctoral", 11500, 1150, 1280, 1035}
    };

    cout << "Welcome to the Buc$ense Budget Game!\n\n";
    cout << "Choose your career education level. Type the number for your selection, then press ENTER:\n";
    for (int index = 0; index < 5; index++) {
        cout << index + 1 << ". " << careers[index].name << endl;
    }

    int choice;
    cin >> choice;
    cin.ignore(); // consume newline
    Career selected = careers[choice - 1];
    double budget = selected.income - selected.taxes - selected.loan - selected.tithing;

    cout << "\nYou chose: " << selected.name << endl;
    displayBudget(budget);
    
    /*This is to make sure that the student knows why
    * their monthly income is the amount that it is.
    */
    if (choice < 3) {
        cout << "This is the amount of money you have to spend each month after taxes and tithing.\n";    
    }
    else {
        cout << "This is the amount of money you have to spend each month after taxes, tithing, and student loan repayment.\n";
    }
    
    // Housing choice
    cout << "\nChoose your home. Type the number for your selection, then press ENTER:\n1. Apartment ($800/month)\n2. Townhouse ($1200/month)\n3. Single Family Home ($1600/month)\n";
    cin >> choice;
    cin.ignore();
    double housingCost = (choice == 1 ? 800 : (choice == 2 ? 1200 : 1600));
    budget -= housingCost;
    cout << "Housing cost: -$" << housingCost << endl;
    displayBudget(budget);

    // Coin flip event #1
    flipCoinEvent("Inherit $1,000", 1000, "Fender bender, pay $1,200", -1200, budget);

    // Transportation choice
    cout << "\nChoose your transportation. Type the number for your selection, then press ENTER:\n1. Hand-me-down ($100/month)\n2. Used ($300/month)\n3. New ($500/month)\n4. Bus ($50/month)\n";
    cin >> choice;
    cin.ignore();
    double transportCost = (choice == 1 ? 100 : (choice == 2 ? 300 : (choice == 3 ? 500 : 50)));
    budget -= transportCost;
    cout << "Transportation cost: -$" << transportCost << endl;
    displayBudget(budget);

    // Short-term savings
    cout << "\nEnter monthly short-term savings amount. Type the number amount you want to save, then press ENTER: $";
    double shortTermSavings;
    cin >> shortTermSavings;
    cin.ignore();
    budget -= shortTermSavings;
    displayBudget(budget);

    // Long-term savings
    cout << "Enter monthly retirement savings amount Type the number amount you want to save, then press ENTER: $";
    double longTermSavings;
    cin >> longTermSavings;
    cin.ignore();
    budget -= longTermSavings;
    displayBudget(budget);
    
    // Coin flip event #2
    flipCoinEvent("Vet bill, pay $500", -500, "Bonus check! +$1500", 1500, budget);

    // Technology (multiple selections)
    cout << "\nChoose your technology. Type 'y' or 'n' for each of the following options:\n";
    double techTotal = 0;
    string input;

    cout << "Cell Phone Bill ($45/month)? "; getline(cin, input); if (input == "y") techTotal += 45;
    cout << "High Speed Internet ($60/month)? "; getline(cin, input); if (input == "y") techTotal += 60;
    cout << "Cable TV ($70/month)? "; getline(cin, input); if (input == "y") techTotal += 70;
    cout << "Streaming Services ($20/month average)? "; getline(cin, input); if (input == "y") techTotal += 20;

    budget -= techTotal;
    cout << "Technology costs: -$" << techTotal << endl;
    displayBudget(budget);

    // Food
    cout << "\nChoose your meals. Type the number for your selection, then press ENTER:\n1. Cook at home ($200/month)\n2. Mix of home and takeout ($600/month)\n3. Eat out often ($1000/month)\n";
    cin >> choice;
    cin.ignore();
    budget -= (choice == 1 ? 200 : (choice == 2 ? 400 : 600));
    displayBudget(budget);

    // Clothing
    cout << "\nChoose your clothing budget. Type the number for your selection, then press ENTER:\n1. Basics/Thrifting ($60/month)\n2. Business Casual ($100/month)\n3. Boutiques/Business Professional ($150/month)\n";
    cin >> choice;
    cin.ignore();
    budget -= (choice == 1 ? 50 : (choice == 2 ? 100 : 200));
    displayBudget(budget);

    // Extra future costs
    cout << "\nDecide on your extra future costs. Type the number for your selection, then press ENTER:\n1. Minimal (Insurance only, $150/month)\n2. Moderate (Insurance + child care, $400/month)\n3. Extensive (Insurace + Childcare + Frequent Car Maintenance, $700/month)\n";
    cin >> choice;
    cin.ignore();
    budget -= (choice == 1 ? 150 : (choice == 2 ? 400 : 700));
    displayBudget(budget);

    // Coin flip event #3
    flipCoinEvent("Stock market crash! Retirement delayed (no budget change)", 0, "Side business success! +$1000", 1000, budget);

    cout << "\nFinal Monthly Budget: $" << budget << endl;

    if (budget >= 0) {
        cout << "You have extra money at the end of the month, so you're financially stable. Great job!\n";
        cout << "You can do with that money as you see fit! Saving or investing it is the wisest long-term choice, though.\n";
    }
    
    else {
        cout << "You're in the red. Consider adjusting your lifestyle choices so that you can actually afford them.\n";
    }

    return 0;
}

void displayBudget(double budget) {
    cout << fixed << setprecision(2);
    cout << "\nCurrent Monthly Budget: $" << budget << endl;
}

double flipCoinEvent(string heads, double headsAmount, string tails, double tailsAmount, double &budget) {
    cout << "\nUnforeseen Event Occurs! Press ENTER to discover your fate...";
    cin.ignore();
    bool isHeads = rand() % 2 == 0;
    if (isHeads) {
        cout << heads << " (" << (headsAmount >= 0 ? "+" : "") << headsAmount << ")\n";
        budget += headsAmount;
    } else {
        cout << tails << " (" << (tailsAmount >= 0 ? "+" : "") << tailsAmount << ")\n";
        budget += tailsAmount;
    }
    displayBudget(budget);
    return budget;
}