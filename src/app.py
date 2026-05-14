import boto3

def main():
    print(boto3.client("s3"))

if __name__ == "__main__":
    main()
