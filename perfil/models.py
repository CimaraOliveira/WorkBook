from django.db import models
from categoria.models import Categoria
from PIL import Image
from django.conf import settings
import os


class Perfil(models.Model):
    nome = models.CharField('nome',max_length=250)
    categorias = models.ManyToManyField(Categoria)
    decricao = models.CharField('descricao', max_length=2000)
    slogan = models.ImageField(upload_to='fotos/%Y/%m/', blank=True, null=True)

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pill = Image.open(img_full_path)
        original_width, original_height = img_pill.size

        if (original_width <= new_width):
            img_pill.close()
            return

        new_height = round((new_width * original_height) / original_width)
        new_img = img_pill.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.slogan:
            self.resize_image(self.slogan, max_image_size)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'perfil'