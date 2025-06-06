# Generated by Django 5.2.1 on 2025-06-02 00:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_nxb_alter_sach_nxb'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='dausach',
            name='MaTG',
            field=models.ManyToManyField(related_name='DauSach', to='api.tacgia'),
        ),
        migrations.AlterField(
            model_name='hoadon',
            name='NguoiLapHD',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='HoaDon', to=settings.AUTH_USER_MODEL, verbose_name='Người lập Hóa Đơn'),
        ),
        migrations.AlterField(
            model_name='phieunhapsach',
            name='NguoiNhap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='PhieuNhapSach', to=settings.AUTH_USER_MODEL, verbose_name='Người nhập'),
        ),
        migrations.AlterField(
            model_name='phieuthutien',
            name='NguoiThu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='PhieuThuTien', to=settings.AUTH_USER_MODEL, verbose_name='Người thu'),
        ),
        migrations.AlterField(
            model_name='sach',
            name='NXB',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sach', to='api.nxb'),
        ),
    ]
