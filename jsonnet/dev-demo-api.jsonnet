local build_and_push_staging(module_name, image_name) = {
  image: "registry.aisingapore.net/sg-nlp/sg-nlp-runner:latest",
  stage: "build_and_push_staging",
  when: "manual",
  script: [
    "echo 'Logging in to AISG Docker Registry...'",
    "echo $STG_REGISTRY_PASSWORD | docker login registry.aisingapore.net -u $STG_DOCKER_USER --password-stdin",
    "echo 'Building and pushing image...'",
    "docker build --no-cache -t %s -f demo_api/%s/dev.Dockerfile ." % [module_name, module_name],
    "docker tag %s registry.aisingapore.net/sg-nlp/%s:latest" % [module_name, image_name],
    "docker push registry.aisingapore.net/sg-nlp/%s:latest" % image_name,
  ],
};


local restart_kubernetes_staging(module_name, deployment_name) = {
  image: "registry.aisingapore.net/sea-core-nlp/seacorenlp-runner:latest",
  stage: "restart_kubernetes_staging",
  when: "manual",
  needs: ["%s_build_and_push_staging" % module_name],
  script: [
    "echo 'Restarting pods...'",
    "export KUBECONFIG=$STG_KUBE_CONFIG",
    "kubectl rollout restart deployment/%s -n sg-nlp-revamp" % deployment_name
  ]
};


local api_names = {
  "rst_pointer": {
    module_name: "rst_pointer",
    image_name: "rst-pointer",
    deployment_name: "rst-pointer"
  },
  "csgec": {
    module_name: "csgec",
    image_name: "csgec",
    deployment_name: "csgec"
  }
};

{
  "stages": [
    "build_and_push_staging",
    "restart_kubernetes_staging",
  ],
} + {
  // Build and push staging
  [api_names[key]["module_name"] + "_build_and_push_staging"]:
    build_and_push_staging(api_names[key]["module_name"], api_names[key]["image_name"])
    for key in std.objectFields(api_names)
} + {
  // Restart kubernetes staging
  [api_names[key]["module_name"] + "_restart_kubernetes_staging"]:
    restart_kubernetes_staging(api_names[key]["module_name"], api_names[key]["deployment_name"])
    for key in std.objectFields(api_names)
}