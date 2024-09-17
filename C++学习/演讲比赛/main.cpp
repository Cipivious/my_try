#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

class Person
{
public:
    std::string serial_number;
    double score;

    Person(int num)
    {
        if (num < 10)
        {
            std::string num_str = std::to_string(num);
            serial_number = "1000" + num_str;
        }
        else
        {
            std::string num_str = std::to_string(num);
            serial_number = "100" + num_str;
        }
        score = 0.0; // Initialize score to 0
    }
};

std::vector<Person *> get_win(std::vector<Person *> &group)
{
    for (int k = 0; k < group.size(); k++)
    {
        int scores[10];
        int max = 0, min = 100;
        for (int i = 0; i < 10; i++)
        {
            scores[i] = rand() % 41 + 60; // Generate random scores
            if (scores[i] > scores[max])
            {
                max = i;
            }
            if (scores[i] < scores[min])
            {
                min = i;
            }
        }
        int sum = 0;
        for (int i = 0; i < 10; i++)
        {
            if (i != max && i != min)
            {
                sum += scores[i];
            }
        }
        double real_score = sum / 8.0;
        group[k]->score = real_score; // Assign the score
    }

    std::sort(group.begin(), group.end(), [](Person *person1, Person *person2)
              { return person1->score > person2->score; });

    std::vector<Person *> result(3); // Create a vector to store top 3
    std::copy(group.begin(), group.begin() + 3, result.begin());

    return result;
}

int main()
{
    std::vector<Person *> players;
    for (int i = 1; i <= 12; i++)
    {
        players.push_back(new Person(i)); // Create new Person objects and store pointers
    }

    std::random_shuffle(players.begin(), players.end());

    std::vector<Person *> group1(6), group2(6);
    std::copy(players.begin(), players.begin() + 6, group1.begin());
    std::copy(players.begin() + 6, players.end(), group2.begin());

    std::vector<Person *> result1 = get_win(group1);
    std::vector<Person *> result2 = get_win(group2);

    std::cout << "Group 1 Winners:\n";
    std::for_each(result1.begin(), result1.end(), [](Person *person)
                  { std::cout << "serial_number: " << person->serial_number << " score: " << person->score << std::endl; });

    std::cout << "--------------------------------------\n";

    std::cout << "Group 2 Winners:\n";
    std::for_each(result2.begin(), result2.end(), [](Person *person)
                  { std::cout << "serial_number: " << person->serial_number << " score: " << person->score << std::endl; });

    std::vector<Person *> finalist;
    finalist.reserve(6); // Reserve space for 6 finalists
    finalist.insert(finalist.end(), result1.begin(), result1.end());
    finalist.insert(finalist.end(), result2.begin(), result2.end());

    std::vector<Person *> final_result = get_win(finalist);

    std::cout << "--------------------------------------\n";
    std::cout << "Final Winners:\n";
    std::for_each(final_result.begin(), final_result.end(), [](Person *person)
                  { std::cout << "serial_number: " << person->serial_number << " score: " << person->score << std::endl; });

    // Cleanup dynamically allocated memory
    for (auto &player : players)
    {
        delete player;
    }

    return 0;
}
