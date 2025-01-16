from smolagents import Tool


class ScrapeTool(Tool):
    name = "scrape_tool"
    description = "This is a tool that downloads the vehicle most recent vehicle data from autotempest.com, and adds the data to the alloydb vectorstore."
    inputs = {}
    output_type = "string"

    def forward(self, task: str) -> str:
        return task
