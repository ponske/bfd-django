# bfd-django
Ubuntu 22 React Django Nginx uwsgi

## セットアップ手順

VPS状にUbuntuをクリーンインストール（VPSプロバイダの画面側から自動操作）
Anacondaをインストール
依存関係パッケージをインストール
Djangoを起動
uWSGIのインストール
Nginxをインストール
ファイアウォールの設定(Nginx Fullポート)
Nginxの起動
サブドメインの設定
UwsgiとDjangoを紐づける
uWSGIの設定ファイル作成（uwsgi_params）※ソケット
NginxとUwsgiを紐づける（uwsgi.ini、mysite_nginx.conf）
Nginx用にシンボリックリンク作成
settings.pyにてドメイン指定
staticファイルを読みこむ（Djangoコマンド）
nginxとuWSGIを自動起動するようにする
サブドメインからのみ閲覧できるようになる
SSL証明書発行（gitのインストール、certbotのクローン、certbot-autoコマンド）
Nginxの設定ファイルをSSL化（mysite_nginx.conf）
ファイアウォールの設定(443番ポート)
Nginx再起動
Djangoマイグレーション
