from django.db import models

# Create your models here.

class HelloWorld(models.Model):
	# objects = models.Manager() # objects 같은 속성들은 model 클래스에 동적으로 추가되기 때문에 vscode에서 사용하기 위해서는 이렇게 명시해두어야 한다.
	text = models.CharField(max_length=255, null=False)