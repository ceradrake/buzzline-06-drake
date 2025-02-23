# buzzline - 06 - drake

I wanted to look at the overall sentiment analysis of news headlines. I am generating fake data for this module versus pulling from real news sources. Each message that is generated will show the source, the headline, and the sentiment analysis of that particular headline. The consumer will then consume that information and create a line chart to reflect the amount of times each sentiment is displayed over a period of time. 

The producer that

We can analyze and visualize different types of streaming data as the information arrives.

The producers don't change from buzzline-03-case - they write the same information to a Kafka topic, except the csv producer for the smart smoker has been modified to not run continuously. It will stop after reading all the rows in the CSV file. 
The consumers have been enhanced to add visualization. 

This project uses matplotlib and its animation capabilities for visualization. 

It generates three applications:

1. A basic producer and consumer that exchange information via a dynamically updated file. 
2. A JSON producer and consumer that exchange information via a Kafka topic. 
3. A CSV producer and consumer that exchange information via a different Kafka topic. 

All three applications produce live charts to illustrate the data. 

## Task 1. Use Tools from Module 1 and 2

Before starting, ensure you have completed the setup tasks in <https://github.com/denisecase/buzzline-01-case> and <https://github.com/denisecase/buzzline-02-case> first. 
Python 3.11 is required. 

## Task 2. Copy This Example Project and Rename

Once the tools are installed, copy/fork this project into your GitHub account
and create your own version of this project to run and experiment with. 
Follow the instructions in [FORK-THIS-REPO.md](https://github.com/denisecase/buzzline-01-case/docs/FORK-THIS-REPO.md).

OR: For more practice, add these example scripts or features to your earlier project. 
You'll want to check requirements.txt, .env, and the consumers, producers, and util folders. 
Use your README.md to record your workflow and commands. 
    

## Task 3. Manage Local Project Virtual Environment

Follow the instructions in [MANAGE-VENV.md](https://github.com/denisecase/buzzline-01-case/docs/MANAGE-VENV.md) to:
1. Create your .venv
2. Activate .venv
3. Install the required dependencies using requirements.txt.

## Task 4. Start Zookeeper and Kafka (2 Terminals)

If Zookeeper and Kafka are not already running, you'll need to restart them.
See instructions at [SETUP-KAFKA.md] to:

1. Start Zookeeper Service ([link](https://github.com/denisecase/buzzline-02-case/blob/main/docs/SETUP-KAFKA.md#step-7-start-zookeeper-service-terminal-1))
2. Start Kafka ([link](https://github.com/denisecase/buzzline-02-case/blob/main/docs/SETUP-KAFKA.md#step-8-start-kafka-terminal-2))

---

## Task 5. Start a Basic (File-based, not Kafka) Streaming Application

This will take two terminals:

1. One to run the producer which writes to a file in the data folder. 
2. Another to run the consumer which reads from the dynamically updated file. 

### Producer Terminal

Start the producer to generate the messages. 

In VS Code, open a NEW terminal.
Use the commands below to activate .venv, and start the producer. 

Windows:

```shell
.venv\Scripts\activate
py -m producers.basic_json_producer_drake
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m producers.basic_json_producer_drake
```

### Consumer Terminal

Start the associated consumer that will process and visualize the messages. 

In VS Code, open a NEW terminal in your root project folder. 
Use the commands below to activate .venv, and start the consumer. 

Windows:
```shell
.venv\Scripts\activate
py -m consumers.basic_json_consumer_drake
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m consumers.basic_json_consumer_drake
```

### Review the Application Code

Review the code for both the producer and the consumer. 
Understand how the information is generated, written to a file, and read and processed. 
Review the visualization code to see how the live chart is produced. 
When done, remember to kill the associated terminals for the producer and consumer. 


---



## Later Work Sessions
When resuming work on this project:
1. Open the folder in VS Code. 
2. Start the Zookeeper service.
3. Start the Kafka service.
4. Activate your local project virtual environment (.env).

## Save Space
To save disk space, you can delete the .venv folder when not actively working on this project.
You can always recreate it, activate it, and reinstall the necessary packages later. 
Managing Python virtual environments is a valuable skill. 

## License
This project is licensed under the MIT License as an example project. 
You are encouraged to fork, copy, explore, and modify the code as you like. 
See the [LICENSE](LICENSE.txt) file for more.

## Live Chart Examples

Live Bar Chart (JSON file streaming)

![Basic JSON (file-exchange)](images/live_bar_chart_basic_example.jpg)

Live Bar Chart (Kafka JSON streaming)

![JSON (Kafka)](images/live_bar_chart_example.jpg)

Live Line Chart with Alert (Kafka CSV streaming)

![CSV (Kafka)](images/live_line_chart_example.jpg)

