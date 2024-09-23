# bfd-django
Ubuntu 22 React Django Nginx uwsgi

## セットアップ手順

1. VPS状にUbuntuをクリーンインストール（VPSプロバイダの画面側から自動操作）
2. Anacondaをインストール
3. 依存関係パッケージをインストール
4. Djangoを起動
5. uWSGIのインストール
6. Nginxをインストール
7. ファイアウォールの設定(Nginx Fullポート)
8. Nginxの起動
9. サブドメインの設定
10. UwsgiとDjangoを紐づける
11. uWSGIの設定ファイル作成（uwsgi_params）※ソケット
12. NginxとUwsgiを紐づける（uwsgi.ini、mysite_nginx.conf）
13. Nginx用にシンボリックリンク作成
14. settings.pyにてドメイン指定
15. staticファイルを読みこむ（Djangoコマンド）
16. nginxとuWSGIを自動起動するようにする
17. サブドメインからのみ閲覧できるようになる
18. SSL証明書発行（gitのインストール、certbotのクローン、certbot-autoコマンド）
19. Nginxの設定ファイルをSSL化（mysite_nginx.conf）
20. ファイアウォールの設定(443番ポート)
21. Nginx再起動
22. Djangoマイグレーション
