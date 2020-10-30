# Usage
コンテナに入る
```
docker-compose up -d --build
docker-compose exec pytest bash
```

テストを実行する
```
pytest tests
```

ホスト側の `/src` はコンテナの `/root/src` にマウントされている。 