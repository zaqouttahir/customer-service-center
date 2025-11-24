from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_agentprofile_agents__routing_341b6f_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentPromptVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tenant_id', models.UUIDField(blank=True, db_index=True, null=True)),
                ('version', models.IntegerField()),
                ('system_prompt', models.TextField()),
                ('metadata', models.JSONField(blank=True, default=dict)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prompt_versions', to='agents.agentprofile')),
            ],
            options={
                'ordering': ['-version'],
                'unique_together': {('agent', 'version')},
            },
        ),
    ]
