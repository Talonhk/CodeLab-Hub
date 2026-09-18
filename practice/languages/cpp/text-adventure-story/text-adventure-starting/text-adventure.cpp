#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <vector>

void intro() {
    std::cout << "Welcome to the Fantasy World Text Adventure!\n";
    std::cout << "You awaken in a misty old forest, with ancient trees looming overhead.\n";
    std::cout << "Paths lead north and east. What will you do?\n";
}

void forest() {
    auto to_lower_trim = [](std::string s) {
        // trim front
        s.erase(s.begin(), std::find_if(s.begin(), s.end(), [](unsigned char ch) { return !std::isspace(ch); }));
        // trim back
        s.erase(std::find_if(s.rbegin(), s.rend(), [](unsigned char ch) { return !std::isspace(ch); }).base(), s.end());
        // to lower
        std::transform(s.begin(), s.end(), s.begin(), [](unsigned char c){ return std::tolower(c); });
        return s;
    };

    auto ask_choice = [&](const std::string &prompt, const std::vector<std::string> &valid) {
        std::string line;
        while (true) {
            std::cout << prompt;
            if (!std::getline(std::cin, line)) {
                // handle EOF by returning the first valid choice as a safe default
                return valid.front();
            }
            line = to_lower_trim(line);
            if (line.empty()) {
                std::cout << "Input was empty. Please try again.\n";
                continue;
            }
            for (const auto &v : valid) if (line == v) return line;
            std::cout << "Please type one of: ";
            for (size_t i = 0; i < valid.size(); ++i) {
                std::cout << '\'' << valid[i] << '\'' << (i + 1 < valid.size() ? ", " : "\n");
            }
        }
    };

    std::string choice;

    // Branch point 1: choose a path
    choice = ask_choice("Type 'north' to go deeper into the forest, or 'east' towards the river: ", {"north","east"});

    if (choice == "north") {
        std::cout << "You venture north and encounter a mysterious old wizard.\n";

        // Branch point 2: accept the quest or not
        choice = ask_choice("He offers you a quest. Do you accept? (yes/no): ", {"yes","no"});

        if (choice == "yes") {
            std::cout << "The wizard smiles and hands you a glowing amulet.\n";
            std::cout << "He asks: will you seek the mountain (type 'mountain') or the ruins (type 'ruins')?\n";

            // Branch point 3: choose the quest destination
            choice = ask_choice("Type 'mountain' or 'ruins': ", {"mountain","ruins"});

            if (choice == "mountain") {
                std::cout << "You climb the misty mountain and discover an ancient dragon asleep on a pile of treasures.\n";
                choice = ask_choice("Do you try to sneak past (type 'sneak') or try to take a gem (type 'take')? ", {"sneak","take"});
                if (choice == "sneak") {
                    std::cout << "You successfully sneak past the dragon and find a hidden shrine. Your wisdom increases.\n";
                } else if (choice == "take") {
                    std::cout << "The dragon wakes and gives you a puzzled look. You are gently escorted off the mountain.\n";
                } else {
                    std::cout << "Hesitation costs you; a sudden storm forces you to retreat.\n";
                }
            } else { // ruins
                std::cout << "You explore the ruined city and uncover a glowing statue that hums with power.\n";
                choice = ask_choice("Do you study the statue ('study') or sell it in the market ('sell')? ", {"study","sell"});
                if (choice == "study") {
                    std::cout << "Studying the statue reveals an old spell; you gain a new magical ability.\n";
                } else if (choice == "sell") {
                    std::cout << "You sell the statue to an antique buyer and gain enough coin to equip yourself.\n";
                } else {
                    std::cout << "You leave the statue untouched and continue your journey unchanged.\n";
                }
            }
        } else {
            std::cout << "The wizard vanishes, leaving you alone in the forest. You find a small map on the ground pointing to a nearby cottage.\n";
            choice = ask_choice("Do you follow the map ('follow') or ignore it and stay in the forest ('stay')? ", {"follow","stay"});
            if (choice == "follow") {
                std::cout << "You follow the map and find a friendly cottage where an old baker offers you food and shelter.\n";
            } else if (choice == "stay") {
                std::cout << "You decide to stay and set up a small camp, listening to the forest at night.\n";
            } else {
                std::cout << "The night grows cold and you eventually head back to the path.\n";
            }
        }

    } else if (choice == "east") {
        std::cout << "You walk east and find a sparkling river. A bridge crosses to the other side.\n";

        // Branch point 2 (alternative path): cross bridge or follow river
        choice = ask_choice("Do you cross the bridge ('cross') or follow the river downstream ('follow')? ", {"cross","follow"});

        if (choice == "cross") {
            std::cout << "On the other side, you discover a hidden village full of friendly elves.\n";
            choice = ask_choice("An elf offers to trade: you can accept a bow ('bow') or a potion ('potion'). Which do you take? ", {"bow","potion"});
            if (choice == "bow") {
                std::cout << "The bow feels light and true in your hands. You feel ready for adventure.\n";
            } else if (choice == "potion") {
                std::cout << "The potion restores some energy and sharpens your senses for the road ahead.\n";
            } else {
                std::cout << "You politely decline and rest in the village for a while.\n";
            }
        } else {
            std::cout << "You follow the river and find a small boat tied to a post.\n";
            choice = ask_choice("Do you take the boat ('boat') or continue walking ('walk')? ", {"boat","walk"});
            if (choice == "boat") {
                std::cout << "You paddle downriver and spot a waterfall with a hidden cave behind it. Adventure awaits.\n";
            } else if (choice == "walk") {
                std::cout << "You walk along the riverbank and find a fishing spot where you catch a delicious meal.\n";
            } else {
                std::cout << "A sudden rainstorm forces you to seek shelter under an old willow.\n";
            }
        }
    }
}

int main() {
    intro();
    forest();
    std::cout << "Thank you for playing!\n";
    return 0;
}