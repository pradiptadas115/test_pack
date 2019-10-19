from core import azure_vm_deploy

__all__ = [
    'deploy_arm_template'
]
class deploy_arm_template(azure_vm_deploy.arm_template_provision):

    def run(self, client_id,resource_group, subscription_number, tanent_id, serect, region, template_file):
        self.auth(client_id,resource_group, subscription_number, tanent_id, serect, region)
        return self.deploy_vm(template_file)