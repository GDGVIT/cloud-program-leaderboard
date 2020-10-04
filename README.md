<p align="center">
<a href="https://dscvit.com">
	<img src="https://user-images.githubusercontent.com/30529572/92081025-fabe6f00-edb1-11ea-9169-4a8a61a5dd45.png" alt="DSC VIT"/>
</a>
	<h2 align="center"> Cloud Program Leaderboard </h2>
	<h4 align="center"> API for #30daysofGCP LeaderBoard <h4>
</p>

---
[![Join Us](https://img.shields.io/badge/Join%20Us-Developer%20Student%20Clubs-red)](https://dsc.community.dev/vellore-institute-of-technology/)

## Functionalities
- [x]  Scrape Public Profiles within seconds
- [x]  Cron Job to update DB

<br>


## Instructions to run


* Fork the repo https://github.com/gdgvit/cloud-program-leaderboard
* Clone the forked repo on to your local machine
* Edit USERS_URLS in ```backend/settings.py``` file with your DSC's Public Profiles.
* Push the code on to your github.
* Create a new app in your heroku
* Go to resources and add ```Heroku Redis```
* And head on to ```settings``` tab and add ```Config Vars```
Config Vars:
```
SECRET_KEY: 20_digit_alphanumerical_key
```
* Now move to ```Deploy``` Tab. And click on deploy with ```Github``` and choose your repo and click on deploy.
* Once done, click on ```Run Console``` which is located inside ```More``` Tab and type the following command <br>```python manage.py migrate```
* Yaay! Your'e done. Click on ```open app```.

## Contributors

<table>
<tr align="center">


<td>

Sai Sandeep <br>Rayanuthala

<p align="center">
<img src = "https://avatars0.githubusercontent.com/u/43823311?s=460&u=e0da23e03034950789b46d08e02c836c4f72f404&v=4" width="150" height="150" alt="Sai Sandeep">
</p>
<p align="center">
<a href = "https://github.com/raysandeep"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36" alt="GitHub"/></a>
<a href = "https://www.linkedin.com/in/sai-sandeep-r/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36" alt="LinkedIn"/>
</a>
</p>
</td>



</tr>
  </table>

<p align="center">
	Made with :heart: by <a href="https://dscvit.com">DSC VIT</a>
</p>

