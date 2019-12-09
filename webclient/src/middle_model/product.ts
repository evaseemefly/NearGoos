class SearchCondition {
  public cateogry: string;
  public area: string;
  public period: string;
  public start: Date;
  public end: Date;
  constructor(
    type: string,
    area: string,
    period: string,
    start: Date,
    end: Date
  ) {
    this.cateogry = type;
    this.area = area;
    this.period = period;
    this.start = start;
    this.end = end;
  }
}

export { SearchCondition };
