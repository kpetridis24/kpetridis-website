from flask import Flask, render_template

app = Flask(__name__)

what_i_do = [
    {
        'name': "High Performance Computing",
        'description': 'I am very good hpc engineer'
    }
]

professional_experience = [
    {
        'company': 'Amazon Web Services',
        'job title': 'Software Development Engineer',
        'period': 'Oct 2022 - Apr 2023',
        'location': 'Dublin, Ireland',
        'description': 'I created new feature'
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