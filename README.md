## Upgrad : House Price Prediction Deployment using Heroku & Docker

## Follow Me:

[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/rakesh-kumar-gupta-52b77ab4/) [<img src = "https://img.shields.io/badge/kaggle-%3390FF.svg?&style=for-the-badge&logo=kaglle&logoColor=white">](https://www.kaggle.com/rakesh6184) [<img src = "https://img.shields.io/badge/twitter-3336FF.svg?&style=for-the-badge&logo=twitter&logoColor=white">](https://twitter.com/2702rakesh) [<img src="https://img.shields.io/badge/medium-%2312100E.svg?&style=for-the-badge&logo=medium&logoColor=white" />](https://medium.com/@2702rakesh)

## Hi there 👋

![Rakesh's github stats](https://github-readme-stats.vercel.app/api?username=RakeshKumar045&show_icons=true)
<img src="https://i.giphy.com/media/LMt9638dO8dftAjtco/200.webp" width="100"><img src="https://i.giphy.com/media/KzJkzjggfGN5Py6nkT/200.webp" width="100"><img src="https://i.giphy.com/media/IdyAQJVN2kVPNUrojM/200.webp" width="100">

### Library Installation :

- pip install -r requirements.txt

### Train the model :

- python model.py

### Predict the model

- python app.py

## Check Demo:

### Click given URL:

<https://upgrad-house-deployment-heroku.herokuapp.com/>

![Image input](./output_photo/browser_output.png "epidemiological model")

### Check the API by Postman :

#### 1) GET Method

- Use given URL in Postman : https://upgrad-house-deployment-heroku.herokuapp.com
- Select GET method
- Click on send

![Image output](./output_photo/output_by_get.png "epidemiological model")

#### 2) POST Method

- Use given URL in Postman : https://upgrad-house-deployment-heroku.herokuapp.com/house_pred
- Select POST method
- Click on Headers : (KEY : Content-Type and VALUE : application/json)
- Click on Body and select raw(use below given json value):

{
"sqft":1500,
"place":2,
"yearsOld":5,
"totalFloor":10,
"bhk":3 }

- Click on send
- Input format:
  ![Image output](./output_photo/input_1.png "epidemiological model")

![Image output](./output_photo/input_2.png "epidemiological model")

-Output:
![Image output](./output_photo/output_by_post.png "epidemiological model")

## Please Star me on GitHub

## Please follow me on GitHub

[<img src="https://img.shields.io/badge/github-%2312100E.svg?&style=for-the-badge&logo=github&logoColor=white" />](https://github.com/RakeshKumar045?tab=repositories)

https://github.com/RakeshKumar045?tab=repositories

![Image github](../github_follow_pic/github.png "epidemiological model")

#### 2nd way deploy application on heroku using Heroku CLI:

## Deployment through Heroku CLI steps:

heroku login

heroku git:clone -a salary-use-heroku-cli-terminal

cd salary-use-heroku-cli-terminal

OR

git init

heroku git:remote -a salary-use-heroku-cli-terminal

git add .

git commit -am "make it better"

git push heroku master

heroku open #check application has deployed successfully & expose the url to

#### Heroku Extra command:

heroku create # heroku create empty app on heroku

git remote -v

heroku logs --tail

heroku ps

heroku local

heroku config

heroku pg:psql # use for DB(PostgreSQL)

## Thank you for reaching out to me on Github. 
