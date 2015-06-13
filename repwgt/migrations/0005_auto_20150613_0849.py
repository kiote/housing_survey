# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repwgt', '0004_auto_20150608_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repwgt',
            old_name='export_year_2011',
            new_name='field_in_2011',
        ),
        migrations.RenameField(
            model_name='repwgt',
            old_name='export_year_2013',
            new_name='field_in_2013',
        ),
        migrations.AddField(
            model_name='repwgt',
            name='export_year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt0',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT0'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt1',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT1'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt10',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT10'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt100',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT100'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt101',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT101'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt102',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT102'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt103',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT103'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt104',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT104'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt105',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT105'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt106',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT106'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt107',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT107'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt108',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT108'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt109',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT109'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt11',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT11'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt110',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT110'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt111',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT111'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt112',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT112'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt113',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT113'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt114',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT114'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt115',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT115'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt116',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT116'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt117',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT117'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt118',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT118'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt119',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT119'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt12',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT12'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt120',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT120'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt121',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT121'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt122',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT122'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt123',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT123'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt124',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT124'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt125',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT125'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt126',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT126'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt127',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT127'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt128',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT128'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt129',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT129'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt13',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT13'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt130',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT130'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt131',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT131'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt132',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT132'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt133',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT133'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt134',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT134'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt135',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT135'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt136',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT136'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt137',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT137'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt138',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT138'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt139',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT139'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt14',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT14'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt140',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT140'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt141',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT141'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt142',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT142'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt143',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT143'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt144',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT144'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt145',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT145'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt146',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT146'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt147',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT147'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt148',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT148'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt149',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT149'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt15',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT15'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt150',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT150'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt151',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT151'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt152',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT152'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt153',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT153'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt154',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT154'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt155',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT155'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt156',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT156'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt157',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT157'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt158',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT158'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt159',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT159'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt16',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT16'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt160',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT160'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt17',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT17'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt18',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT18'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt19',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT19'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt2',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT2'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt20',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT20'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt21',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT21'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt22',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT22'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt23',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT23'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt24',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT24'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt25',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT25'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt26',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT26'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt27',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT27'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt28',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT28'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt29',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT29'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt3',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT3'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt30',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT30'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt31',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT31'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt32',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT32'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt33',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT33'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt34',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT34'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt35',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT35'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt36',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT36'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt37',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT37'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt38',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT38'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt39',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT39'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt4',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT4'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt40',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT40'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt41',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT41'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt42',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT42'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt43',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT43'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt44',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT44'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt45',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT45'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt46',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT46'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt47',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT47'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt48',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT48'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt49',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT49'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt5',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT5'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt50',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT50'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt51',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT51'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt52',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT52'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt53',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT53'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt54',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT54'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt55',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT55'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt56',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT56'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt57',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT57'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt58',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT58'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt59',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT59'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt6',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT6'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt60',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT60'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt61',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT61'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt62',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT62'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt63',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT63'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt64',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT64'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt65',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT65'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt66',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT66'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt67',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT67'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt68',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT68'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt69',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT69'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt7',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT7'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt70',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT70'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt71',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT71'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt72',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT72'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt73',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT73'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt74',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT74'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt75',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT75'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt76',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT76'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt77',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT77'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt78',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT78'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt79',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT79'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt8',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT8'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt80',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT80'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt81',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT81'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt82',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT82'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt83',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT83'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt84',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT84'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt85',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT85'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt86',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT86'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt87',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT87'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt88',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT88'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt89',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT89'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt9',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT9'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt90',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT90'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt91',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT91'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt92',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT92'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt93',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT93'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt94',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT94'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt95',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT95'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt96',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT96'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt97',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT97'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt98',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT98'),
        ),
        migrations.AlterField(
            model_name='repwgt',
            name='repwgt99',
            field=models.DecimalField(null=True, decimal_places=10, max_digits=20, db_column=b'REPWGT99'),
        ),
    ]
