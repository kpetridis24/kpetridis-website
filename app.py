from flask import Flask, render_template

app = Flask(__name__)

what_i_do = [
    {
        'name': "High Performance Computing",
        'description': 'I am very good hpc engineer'
    },
    {
        'name': "Backend Engineering",
        'description': 'I am very good backend engineer'
    },
    {
        'name': "Computer Graphics",
        'description': 'I am very good graphics engineer'
    },
    {
        'name': "Distributed Systems",
        'description': 'I am very good graphics engineer'
    }
]

professional_experience = [
    {
        'company': 'Amazon Web Services',
        'job title': 'Software Development Engineer',
        'period': 'Oct 2022 - Apr 2023',
        'location': 'Dublin, Ireland',
        'description': 'Worked on infrastructures that guarantee high scalability, durability and fault tolerance of '
                       'database systems. Took complete ownership and developed code in the services, responsible for '
                       'scheduling and executing the brand new tasks, across distributed components of the '
                       'infrastructure. Developed, tested and debugged code using Java, Bash, JUnit, Spring, deployed '
                       'changes in pre-prod environments to perform end-to-end tests on RDS instances, designed parts '
                       'of the new product and found solutions to guarantee code maintainability, idempotence and '
                       're-usability for future implementations.'
    },

    {
        'company': 'SpaceDot',
        'job title': 'Software Engineer',
        'period': 'Jan 2021 - Nov 2022',
        'location': 'Thessaloniki, Greece',
        'description': 'Software Engineer in the AcubeSAT, a nano-satellite, able to conduct biological experiments '
                       'related to cell adaptation on board. The satellite is scheduled to be launched into space, in '
                       'collaboration with the European Space Agency (ESA). Developed the On-Board Software Services, '
                       'responsible for message parsing, telecommand processing, task triggering, telemetry creation,'
                       ' parameter sampling, storing and housekeeping, statistics calculation/reporting, error '
                       'handling/logging, MCU synchronisation and communication. Also segmentation of the images '
                       'captured during the biological experiment. Used C, C++, STL, ETL, ATSAM microcontrollers, '
                       'FreeRTOS, Boost, MPLabX, Catch2'
    },

    {
        'company': 'NumFOCUS',
        'job title': 'GSoC contributor',
        'period': 'May 2022 - Oct 2022',
        'location': 'Remote',
        'description': 'Implemented and improved VF2++, a state-of-the-art algorithm for multi and directed graph '
                       'settings and extended it for the Monomorphism and Subgraph Isomorphism problems. Used Python, '
                       'NetworkX, CProfile, IPython. Achieved up to 15X and 30X speedup respectively, for dense and '
                       'sparse graphs, compared to the previous Isomorphism solvers of the library, while also '
                       'decreasing memory consumption significantly.'
    }
]

full_name = 'Konstantinos Petridis'
job_title = 'Software Engineer'

@app.route('/')
def website():
    return render_template('home.html',
                           full_name=full_name,
                           job_title=job_title,
                           personal_interests=what_i_do,
                           professional_experience=professional_experience)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)