# AWS lambda with S3

```bash
pip install --target ./package pyYaml==5.1 jejunuMeals==1.4
zip -r9 ./function.zip ./package
zip -g function.zip lambda_function.py
aws lambda update-function-code --function-name jejunu-meals --zip-file fileb://function.zip
```

https://www.frontend.moe/posts/aws-lambda-with-s3/
