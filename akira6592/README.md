# このワークスペースの目的

Ansible の Playobook 作成

# どんなことをしたくて設定を入れているか

ファイルの保存時に、Playbook の syntax check や、lint（ansible-lint/yamllint）がかかるようにしています。

各種チェックのタスクを `tasks.json` に定義し、そのタスクを [Trigger Task on Save](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.triggertaskonsave) という拡張経由で呼び出します。 

また、お試し中ですが、拡張 [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) と ansible 系の JSON Schema の組み合わせて、Playbook の

# 相談したい、話したいこと（任意）

本当はファイル保存前にリアルタイムにかけられるようになるといいなと思っています。

別のアプローチでもっとスマートな方法もあるかもしれません。

他、これからやりたいのは

- ansible-lint 5.x への対応
- syntax-check の改善
- ansible 2.10 への対応
