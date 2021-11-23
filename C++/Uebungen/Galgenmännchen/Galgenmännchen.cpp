// Galgenmännchen.cpp : Diese Datei enthält die Funktion "main". Hier beginnt und endet die Ausführung des Programms.
//

#include <iostream>
#include <string>

int main()
{
    std::string hang1 = " +---+\n";
    hang1.append(" |   |\n");
    hang1.append("     |\n");
    hang1.append("     |\n");
    hang1.append("     |\n");
    hang1.append("     |\n");
    hang1.append("========");

    std::string hang2 = " +---+\n";
    hang2.append(" |   |\n");
    hang2.append(" O   |\n");
    hang2.append("     |\n");
    hang2.append("     |\n");
    hang2.append("     |\n");
    hang2.append("========");

    std::string hang3 = " +---+\n";
    hang3.append(" |   |\n");
    hang3.append(" O   |\n");
    hang3.append(" |   |\n");
    hang3.append("     |\n");
    hang3.append("     |\n");
    hang3.append("========");

    std::string hang4 = " +---+\n";
    hang4.append(" |   |\n");
    hang4.append(" O   |\n");
    hang4.append("/|   |\n");
    hang4.append("     |\n");
    hang4.append("     |\n");
    hang4.append("========");

    std::string hang5 = " +---+\n";
    hang5.append(" |   |\n");
    hang5.append(" O   |\n");
    hang5.append("/|\\  |\n");
    hang5.append("     |\n");
    hang5.append("     |\n");
    hang5.append("========");

    std::string hang6 = " +---+\n";
    hang6.append(" |   |\n");
    hang6.append(" O   |\n");
    hang6.append("/|\\  |\n");
    hang6.append("/    |\n");
    hang6.append("     |\n");
    hang6.append("========");

    std::string hang7 = " +---+\n";
    hang7.append(" |   |\n");
    hang7.append(" O   |\n");
    hang7.append("/|\\  |\n");
    hang7.append("/ \\  |\n");
    hang7.append("     |\n");
    hang7.append("========");

    std::string hangs[7] = {
        hang1, hang2, hang3, hang4, hang5, hang6, hang7
    };

    std::string guess_word;
    std::string display_word;
    std::cout << "Geben Sie das zu erratende Wort ein: ";
    std::cin >> guess_word;
    for (int i = 0; i < guess_word.length(); i++) {
        guess_word[i] = toupper(guess_word[i]);
    }
    for (int i = 0; i < guess_word.length(); i++) {
        display_word.append("-");
    }

    char guess;

    int errors = 0;

    bool run = true;

    std::system("CLS");
    

    while (run) {
        std::cout << display_word << std::endl;
        std::cout << hangs[errors] << std::endl;
        std::cout << "Raten Sie einen Buchstaben! \n";
        std::cin >> guess;
        // right guess
        if (guess_word.find(toupper(guess)) != std::string::npos) {
            //search for string
            for (int i = 0; i < guess_word.length(); i++) {
                if (guess_word[i] == toupper(guess)) {
                    display_word[i] = toupper(guess);
                }
            }
        }
        else {
            errors++;
        }
        std::system("CLS");
        // lost
        if (errors >= 6) {
            std::cout << hangs[errors] << std::endl;
            std::cout << "Leider verloren! Das Wort war " + guess_word;
            run = false;
        }
        // won
        else if (display_word.find('-') == std::string::npos) {
            std::cout << display_word << std::endl;
            std::cout << "Glueckwunsch, du hast das Wort erraten!";
            run = false;
        }
    }
}