from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
class Game(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2')
    moves = models.TextField()
    result = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)