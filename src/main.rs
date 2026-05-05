use tokio::runtime::Runtime;

fn main() {
    let rt = Runtime::new().expect("failed to create runtime");
    rt.block_on(async {
        println!("hello from tokio");
    });
}
