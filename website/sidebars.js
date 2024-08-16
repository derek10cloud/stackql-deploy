// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docsSidebar: [
    {
      type: 'doc',
      id: 'index', 
      label: 'Welcome',
    },
    {
      type: 'doc',
      id: 'getting-started', 
      label: 'Getting Started',
    },
    {
      type: 'category',
      label: 'CLI Command Reference',
      items: [
        'cli-reference/build',
        'cli-reference/init',
        'cli-reference/teardown',
        'cli-reference/test',
        'cli-reference/info',
        'cli-reference/upgrade',
      ],
    },
    {
      type: 'doc',
      id: 'manifest-file', 
      label: 'stackql_manifest.yml',
    },    
    {
      type: 'doc',
      id: 'resource-query-files', 
      label: 'Resource Query Files',
    },    
    {
      type: 'doc',
      id: 'github-actions', 
      label: 'Deploying with GitHub Actions',
    },
    {
      type: 'category',
      label: 'Template Library',
      link: {
        type: 'generated-index',
        title: 'Template Library',
        description: 'stackql-deploy quick starts, how-tos, practical examples and use cases',
        slug: '/template-library',
        keywords: ['quickstarts', 'guides', 'how-tos', 'examples', 'use cases'],
      },
      items: [
        {
          type: 'category',
          label: 'AWS',
          description: 'Practical examples and use cases specific to AWS',
          customProps: {
            icon: 'img/providers/aws/aws.png',
          },
          link: {
            type: 'generated-index',
            title: 'stackql-deploy AWS Templates',
            description: 'Practical examples and use cases specific to AWS',
            slug: '/template-library/aws',
          },
          items: [{ type: 'autogenerated', dirName: 'template-library/aws' }],
        },
        {
          type: 'category',
          label: 'Microsoft Azure',
          description: 'Practical examples and use cases specific to Azure',
          customProps: {
            icon: 'img/providers/azure/azure.png',
          },          
          link: {
            type: 'generated-index',
            title: 'stackql-deploy Azure Templates',
            description: 'Practical examples and use cases specific to Azure',
            slug: '/template-library/azure',
          },
          items: [{ type: 'autogenerated', dirName: 'template-library/azure' }],
        },
        {
          type: 'category',
          label: 'Google Cloud Platform',
          description: 'Practical examples and use cases specific to Google Cloud',
          customProps: {
            icon: 'img/providers/google/google.png',
          },          
          link: {
            type: 'generated-index',
            title: 'stackql-deploy Google Templates',
            description: 'Practical examples and use cases specific to Google Cloud',
            slug: '/template-library/google',
          },
          items: [{ type: 'autogenerated', dirName: 'template-library/google' }],
        },
      ],
    },
  ],
};

export default sidebars;
